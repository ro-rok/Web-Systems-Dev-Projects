from flask import Blueprint, redirect, request, render_template, url_for

from sql.db import DB
sample = Blueprint('sample', __name__, url_prefix='/sample')


@sample.route('/add', methods=['GET', 'POST'])
def add():
    k = request.form.get("key", None)
    v = request.form.get("value", None)
    resp = None
    if k and v:
        try:
            result = DB.insertOne(
                "INSERT INTO IS601_Sample (name, val) VALUES(%s, %s)", k, v)
            if result.status:
                resp = "Saved record"
        except Exception as e:
            resp = e

    return render_template("add_sample.html", resp=resp)

@sample.route('/list', methods=['GET'])
def list():
    key = request.args.get("name")
    col = request.args.get("col")
    order = request.args.get("order")
    limit = request.args.get("limit", 10)
    args = []
    print(f"col {col} order {order}")
    # dynamically build our query and data mappings
    # use the WHERE true trick so we can easily append conditions without caring if a condition
    # already was applied (no need to check if WHERE exists)
    query = "SELECT id, name, val, created, modified from IS601_Sample WHERE 1=1"
    if key:
        query += " AND name like %s"
        args.append(f"%{key}%")
    if col and order:
        # incorrect
        # these get passed as safe strings rather than sql keywords
        # query += f" ORDER BY %s %s"
        # args.append(col)
        # args.append(order)
        # correct - validate fully that col and order are expected values
        # this will be directly injected and if not validated could
        # lead to sql injection
        if col in ["name","val","created","modified"] \
            and order in ["asc", "desc"]:
            query += f" ORDER BY {col} {order}"

    if limit and int(limit) > 0 and int(limit) <= 100:
        # technically this should follow the same rules as col/order
        # but it seems to work with the placeholder mapping with
        # this connector
        query += " LIMIT %s"
        args.append(int(limit))
    rows = []
    error = None
    try:
        # convert our list to args via *
        print(query)
        resp = DB.selectAll(query, *args)
        if resp.status:
            rows = resp.rows
    except Exception as e:
        error = e
    
    return render_template("list_sample.html", resp=rows, error=error)