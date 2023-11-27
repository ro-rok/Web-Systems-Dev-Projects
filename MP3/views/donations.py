import datetime
from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import re
donations = Blueprint('donations', __name__, url_prefix='/donations')


@donations.route("/search", methods=["GET"])
def search():
    rows = []
    organization_name = ""
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve donation id as id, donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments, organization_name using a LEFT JOIN
    # rk868 11/25/23
    query = """SELECT d.id, d.donor_firstname, d.donor_lastname, d.donor_email, d.organization_id, d.item_name, d.item_description, d.item_quantity, d.donation_date, d.comments, o.name
            FROM IS601_MP3_Donations as d LEFT JOIN IS601_MP3_Organizations as o ON d.organization_id = o.id WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["donor_firstname", "donor_lastname", "donor_email", "organization_name" ,"item_name", "item_quantity", "created", "modified"]
    
    # TODO search-2 get fn, ln, email, organization_id, column, order, limit from request args
    # rk868 11/25/23
    fn = request.args.get("fn")
    ln = request.args.get("ln")
    email = request.args.get("email")
    organization_id = request.args.get("organization_id")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit")
    
    # TODO search-3 append like filter for donor_firstname if provided
    # rk868 11/25/23
    if fn:
        query += " AND d.donor_firstname LIKE %(fn)s"
        args["fn"] = f"%{fn}%"
    
    # TODO search-4 append like filter for donor_lastname if provided
    # rk868 11/25/23
    if ln:
        query += " AND d.donor_lastname LIKE %(ln)s"
        args["ln"] = f"%{ln}%"
    
    # TODO search-5 append like filter for donor_email if provided
    # rk868 11/25/23
    if email:
        query += " AND d.donor_email LIKE %(email)s"
        args["email"] = f"%{email}%"

    # TODO search-6 append like filter for item_name if provided
    # rk868 11/25/23
    item_name = request.args.get("item_name")
    if item_name:
        query += " AND d.item_name LIKE %(item_name)s"
        args["item_name"] = f"%{item_name}%"

    # TODO search-7 append equality filter for organization_id if provided
    # rk868 11/25/23
    if organization_id:
        query += " AND d.organization_id = %(organization_id)s"
        args["organization_id"] = organization_id
    
    # TODO search-8 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    # rk868 11/25/23
    if column and order and column in allowed_columns and order in ["asc", "desc"]:
        query += f" ORDER BY {column} {order}"
    
    # TODO search-9 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # rk868 11/25/23
    if limit:
        try:
            limit = int(limit)
            if limit > 0 and limit <= 100:
                query += " LIMIT %(limit)s"
                args["limit"] = limit
    #print("query",query)
    #print("args", args)
        except ValueError:
            flash("Limit must be a number", "danger")
    # TODO search-10 provide a proper error message if limit isn't a number or if it's out of bounds
    # rk868 11/25/23
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-11 make message user friendly
        # rk868 11/25/23
        flash(str(e), "danger")
    
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    
    # TODO search-12 if request args has organization identifier set organization_name variable to the correct name
    # rk868 11/25/23
    organization_id = request.args.get("organization_id")
    if organization_id:
        try:
            result = DB.selectOne("SELECT name FROM IS601_MP3_Organizations WHERE id = %s", organization_id)
            if result.status:
                organization_name = result.row.get("name")
        except Exception as e:
            flash(str(e), "danger")
    
    allowed_columns = [(c, c.replace("_", " ").title()) for c in allowed_columns]
    
    return render_template("list_donations.html", organization_name=organization_name, rows=rows, allowed_columns=allowed_columns)


@donations.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
        # rk868 11/25/23
        donor_firstname = request.form.get("donor_firstname")
        donor_lastname = request.form.get("donor_lastname")
        donor_email = request.form.get("donor_email")
        organization_id = request.form.get("organization_id")
        item_name = request.form.get("item_name")
        item_description = request.form.get("item_description")
        item_quantity = request.form.get("item_quantity")
        donation_date = request.form.get("donation_date")
        comments = request.form.get("comments")
        
        # TODO add-2 donor_firstname is required (flash proper error message)
        # rk868 11/25/23
        if not donor_firstname:
            flash("Donor First Name is required", "danger")
            has_error = True
        
        # TODO add-3 donor_lastname is required (flash proper error message)
        # rk868 11/25/23
        if not donor_lastname:
            flash("Donor Last Name is required", "danger")
            has_error = True

        # TODO add-4 donor_email is required (flash proper error message)
        # rk868 11/25/23
        if not donor_email:
            flash("Donor Email is required", "danger")
            has_error = True
        # TODO add-4a email must be in proper format (flash proper message)
        # rk868 11/25/23
        if donor_email and not re.match(r"[^@]+@[^@]+\.[^@]+", donor_email):
            flash("Invalid Email Format", "danger")
            has_error = True
        
        # TODO add-5 organization_id is required (flash proper error message)
        # rk868 11/25/23
        if not organization_id:
            flash("Organization ID is required", "danger")
            has_error = True
        
        # TODO add-6 item_name is required (flash proper error message)
        # rk868 11/25/23
        if not item_name:
            flash("Item Name is required", "danger")
            has_error = True
        
        # TODO add-7 item_description is optional
        # rk868 11/25/23
        if not item_description:
            flash("Item Description is absent", "warning")
                
        # TODO add-8 item_quantity is required and must be more than 0 (flash proper error message)
        # rk868 11/25/23
        if not item_quantity:
            flash("Item Quantity is required", "danger")
            has_error = True
        elif int(item_quantity) <= 0:
            flash("Item Quantity must be more than 0", "danger")
            has_error = True
        
        # TODO add-9 donation_date is required and must be within the past 30 days
        # rk868 11/25/23
        if not donation_date:
            flash("Donation Date is required", "danger")
            has_error = True
        else:
            donation_date = datetime.datetime.strptime(donation_date, "%Y-%m-%d")
            current_date = datetime.datetime.now()
            if (current_date - donation_date).days > 30:
                flash("Donation Date must be within the past 30 days", "danger")
                has_error = True
        
        # TODO add-10 comments are optional
        # rk868 11/25/23
        if not comments:
            flash("Comments are absent", "warning")

        has_error = False # use this to control whether or not an insert occurs
        
        if not has_error:
            try:
                result = DB.insertOne("""
                            INSERT INTO IS601_MP3_Donations 
                            (donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """, donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments)

                if result.status:
                    print("donation record created")
                    flash("Created Donation Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                print(f"insert error {e}")
                flash("Error Creating Donation Record", "danger")
    return render_template("manage_donation.html",donation=request.form)

@donations.route("/edit", methods=["GET", "POST"])
def edit():
    row = {}
    
    # TODO edit-1 request args id is required (flash proper error message)
    # rk868 11/25/23
    donation_id = request.args.get("id")
    if not donation_id:
        flash("Donation ID is required for editing", "danger")
        return redirect(url_for("donations.search"))
    else:
        if request.method == "POST":            
            # TODO add-2 retrieve form data for donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
            # rk868 11/25/23
            form_data = request.form
            donor_firstname = form_data.get("donor_firstname")
            donor_lastname = form_data.get("donor_lastname")
            donor_email = form_data.get("donor_email")
            organization_id = form_data.get("organization_id")
            item_name = form_data.get("item_name")
            item_description = form_data.get("item_description")
            item_quantity = form_data.get("item_quantity")
            donation_date = form_data.get("donation_date")
            comments = form_data.get("comments")
            
            # TODO add-3 donor_firstname is required (flash proper error message)
            # rk868 11/25/23
            if not donor_firstname:
                flash("Donor First Name is required", "danger")
                has_error = True
            
            # TODO add-4 donor_lastname is required (flash proper error message)
            # rk868 11/25/23
            if not donor_lastname:
                flash("Donor Last Name is required", "danger")
                has_error = True
            
            # TODO add-5 donor_email is required (flash proper error message)
            # TODO add-5a email must be in proper format (flash proper message)
            # rk868 11/25/23
            if not donor_email:
                flash("Donor Email is required", "danger")
                has_error = True
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", donor_email):
                flash("Invalid Email format", "danger")
                has_error = True
            
            # TODO add-6 organization_id is required (flash proper error message)
            # rk868 11/25/23
            if not organization_id:
                flash("Organization ID is required", "danger")
                has_error = True
            
            # TODO add-7 item_name is required (flash proper error message)
            # rk868 11/25/23
            if not item_name:
                flash("Item Name is required", "danger")
                has_error = True

            # TODO add-8 item_description is optional
            # rk868 11/25/23
            if not item_description:
                flash("Item Description is absent", "warning")

            # TODO add-9 item_quantity is required and must be more than 0 (flash proper error message)
            # rk868 11/25/23
            if not item_quantity:
                flash("Item Quantity is required", "danger")
                has_error = True
            elif int(item_quantity) <= 0:
                flash("Item Quantity must be more than 0", "danger")
                has_error = True
            
            # TODO add-10 donation_date is required and must be within the past 30 days
            # rk868 11/25/23
            if not donation_date:
                flash("Donation Date is required", "danger")
                has_error = True
            
            # TODO add-11 comments are optional
            # rk868 11/25/23
            if not comments:
                flash("Comments are absent", "warning")
            
            has_error = False # use this to control whether or not an update occurs
            
            if not has_error:
                try:
                    # TODO edit-12 fill in proper update query
                    result = DB.update("""
                    UPDATE IS601_MP3_Donations SET donor_firstname = %s, donor_lastname = %s, donor_email = %s, 
                                    organization_id = %s, item_name = %s, item_description = %s, 
                                    item_quantity = %s, donation_date = %s, comments = %s
                    WHERE id = %s
                    """, donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description,
                        item_quantity, donation_date, comments, donation_id)

                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-13 make this user-friendly
                    print(f"update error {e}")
                    flash("Error updating record", "danger")
        
        try:
            # TODO edit-14 fetch the updated data 
            result = DB.selectOne("""SELECT id, donor_firstname, donor_lastname, donor_email, organization_id, 
                                        item_name, item_description, item_quantity, donation_date, comments
                            FROM IS601_MP3_Donations WHERE id = %s""", donation_id)
            
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-15 make this user-friendly
            flash("Error fetching record", "danger")
    
    return render_template("manage_donation.html", donation=row)

@donations.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 if id is missing, flash necessary message and redirect to search
    # rk868 11/25/23
    donation_id = request.args.get("id")
    if not donation_id:
        flash("Donation ID is required for deletion", "danger")
        return redirect(url_for("donations.search"))

    try:

    # TODO delete-2 delete donation by id (fetch the id from the request)
    # rk868 11/25/23
        result = DB.delete("DELETE FROM IS601_MP3_Donations WHERE id = %s", donation_id)
    
    
    # TODO delete-3 ensure a flash message shows for successful delete
    # rk868 11/25/23
        if result.status:
            flash("Deleted record", "success")
    
    # TODO delete-4 pass all argument except id to this route
    # rk868 11/25/23
    except Exception as e:
        flash("Error deleting record", "danger")
    
    # TODO delete-5 redirect to donation search
    # rk868 11/25/23

    return redirect(url_for("donations.search", **request.args))
