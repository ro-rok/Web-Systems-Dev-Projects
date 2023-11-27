from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB

import pycountry
organization = Blueprint('organization', __name__, url_prefix='/organization')

@organization.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, donation count as donations for the organization
    #rk868 11/26/23
    # don't do SELECT * and replace the below "..." portion
    allowed_columns = ["name", "city", "country", "state", "modified", "created"]
    
    query = """
        SELECT o.id, o.name, o.address, o.city, o.country, o.state, o.zip, o.website, COUNT(d.id) AS donations, o.modified, o.created
        FROM IS601_MP3_Organizations AS o
        LEFT JOIN IS601_MP3_Donations AS d ON o.id = d.organization_id
        WHERE 1=1
        GROUP BY o.id, o.name, o.address, o.city, o.country, o.state, o.zip, o.website 
    """
    args = {} # <--- add values to replace %s/%(named)s placeholders

    
    # TODO search-2 get name, country,S state, column, order, limit request args
    #rk868 11/26/23
    name = request.args.get("name")
    country = request.args.get("country")
    state = request.args.get("state")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit")
    
    print(name)
    print(type(country))
    print(state)

    # TODO search-3 append a LIKE filter for name if provided
    #rk868 11/26/23
    if name:
        query += " AND name LIKE %(name)s"
        args["name"] = f"%{name}%"
    
    # TODO search-4 append an equality filter for country if provided
    #rk868 11/26/23
    if country:
        query += " AND country = %(country)s"
        args["country"] = country
    
    # TODO search-5 append an equality filter for state if provided
    #rk868 11/26/23
    if state:
        query += " AND state = %(state)s"
        args["state"] = state
    
    # TODO search-6 append sorting if column and order are provided and within the allows columns and allowed order asc,desc
    #rk868 11/26/23
    if column and order and column in allowed_columns and order in ["asc", "desc"]:
        query += f" ORDER BY {column} {order}"
    
    # TODO search-7 append limit (default 10) or limit greater than or equal to 1 and less than or equal to 100
    #rk868 11/26/23
    if limit:
        try:
            limit = int(limit)
            if limit >= 1 and limit <= 100:
                query += " LIMIT %(limit)s"
                args["limit"] = limit
            else:
                flash("Limit must be between 1 and 100", "danger")
        except ValueError:
            flash("Limit must be a number", "danger")
    
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-9 make message user friendly
        print(f"{e}")
        flash("Error retrieving organizations", "danger")
    
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    allowed_columns = [(c, c.replace("_", " ").title()) for c in allowed_columns]

    return render_template("list_organizations.html", rows=rows, allowed_columns=allowed_columns)


@organization.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        has_error = False # use this to control whether or not an insert occurs
        
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website, description
        #rk868 11/27/23
        name = request.form.get("name")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        zip_code = request.form.get("zip")
        website = request.form.get("website")
        description = request.form.get("description")
        
        # TODO add-2 name is required (flash proper error message)
        #rk868 11/27/23
        if not name:
            flash("Name is required", "danger")
            has_error = True
        
        # TODO add-3 address is required (flash proper error message)
        #rk868 11/27/23
        if not address:
            flash("Address is required", "danger")
            has_error = True

        # TODO add-4 city is required (flash proper error message)
        #rk868 11/27/23
        if not city:
            flash("City is required", "danger")
            has_error = True
        
        # TODO add-5 state is required (flash proper error message)
        #rk868 11/27/23
        if not state:
            flash("State is required", "danger")
            has_error = True
        
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        #rk868 11/27/23
        if country.strip():
            states = pycountry.subdivisions.get(country_code=country.strip())
        if not states:
            states = []
        valid_states = [state.code.split("-")[1] for state in states]
        if state not in valid_states:
            flash("Invalid State", "danger")
            has_error = True
    
        # TODO add-6 country is required (flash proper error message)
        #rk868 11/27/23
        if not country:
            flash("Country is required", "danger")
            has_error = True
        
        # TODO add-6a country should be a valid country mentioned in pycountry from country = country code
        #rk868 11/27/23
        valid_countries = [country.alpha_2 for country in list(pycountry.countries)]
        if country not in valid_countries:
            flash("Invalid Country", "danger")
            has_error = True
        
        # TODO add-7 website is not required
        if not website:
            flash("Website is absent", "warning")
        
        # TODO add-8 zip is required (flash proper error message)
        #rk868 11/27/23
        if not zip_code:
            flash("Zip is required", "danger")
            has_error = True
        
        # TODO add-9 description is not required
        if not description:
            flash("Description is absent", "warning")
        
        # TODO add-10 add query and add arguments
        # rk868 11/27/23
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Organizations (name, address, city, state, country, zip, website, description)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, name, address, city, state, country, zip_code, website, description)
                
                if result.status:
                    flash("Added Organization", "success")
            except Exception as e:
                # TODO add-11 make message user friendly
                print(f"{e}")
                flash("Error adding organization", "danger")
        
    return render_template("manage_organization.html", org=request.form)

@organization.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    # rk868 11/27/23
    id = request.args.get("id")
    if not id:
        flash("ID is required for editing", "danger")
        return redirect(url_for("organization.search"))
    else:
        if request.method == "POST":
            # TODO edit-2 retrieve form data for name, address, city, state, country, zip, website
            # rk868 11/27/23
            name = request.form.get("name")
            address = request.form.get("address")
            city = request.form.get("city")
            state = request.form.get("state")
            country = request.form.get("country")
            zip_code = request.form.get("zip")
            website = request.form.get("website")
            description = request.form.get("description")
            
            # TODO edit-3 name is required (flash proper error message)
            # rk868 11/27/23
            if not name:
                flash("Name is required", "danger")
                has_error = True

            # TODO edit-4 address is required (flash proper error message)
            # rk868 11/27/23
            if not address:
                flash("Address is required", "danger")
                has_error = True
            
            # TODO edit-5 city is required (flash proper error message)
            # rk868 11/27/23
            if not city:
                flash("City is required", "danger")
                has_error = True

            # TODO edit-6 state is required (flash proper error message)
            # rk868 11/27/23
            if not state:
                flash("State is required", "danger")
                has_error = True
            
            # TODO edit-6a state should be a valid state mentioned in pycountry for the selected state
            # rk868 11/27/23
            if country.strip():
                states = pycountry.subdivisions.get(country_code=country.strip())
            if not states:
                states = []
            valid_states = [state.code.split("-")[1] for state in states]
            if state not in valid_states:
                flash("Invalid State", "danger")
                has_error = True
            
            # TODO edit-7 country is required (flash proper error message)
            # rk868 11/27/23
            if not country:
                flash("Country is required", "danger")
                has_error = True
            
            # TODO edit-7a country should be a valid country mentioned in pycountry
            # rk868 11/27/23
            valid_countries = [country.alpha_2 for country in list(pycountry.countries)]
            if country not in valid_countries:
                flash("Invalid country", "danger")
                has_error = True
            
            # TODO edit-8 website is not required
            # rk868 11/27/23
            if not website:
                flash("Website is absent", "warning")
            
            # TODO edit-9 zipcode is required (flash proper error message)
            # rk868 11/27/23
            if not zip_code:
                flash("Zipcode is required", "danger")
                has_error = True
            
            has_error = False

            # TODO edit-10 fill in proper update query
            # rk868 11/27/23
            if not has_error:
                print("Updating organization")
                try:
                    result = DB.update("""
                    UPDATE IS601_MP3_Organizations
                    SET name = %s, address = %s, city = %s, state = %s, country = %s, zip = %s, website = %s, description = %s
                    WHERE id = %s
                    """, name, address, city, state, country, zip_code, website, description, id)
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    print(f"{e}")
                    print(e)
                    flash("Error updating organization", "danger")
        
        row = {}
        try:
            # TODO edit-12 fetch the updated data
            # rk868 11/27/23
            result = DB.selectOne("SELECT * FROM IS601_MP3_Organizations WHERE id = %s", id)
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-13 make this user-friendly
            # rk868 11/27/23
            print(f"{e}")
            flash("Error fetching record", "danger")
    
    return render_template("manage_organization.html", org=row)

@organization.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 if id is missing, flash necessary message and redirect to search
    # rk868 11/27/23
    organization_id = request.args.get("id")
    if not organization_id:
        flash("Organization ID is required for deletion", "danger")
        return redirect(url_for("organization.search"))

    try:
        # TODO delete-2 delete organization by id (fetch the id from the request)
        # rk868 11/27/23
        
        intermediate_result = DB.delete("DELETE FROM IS601_MP3_Donations WHERE organization_id = %s", organization_id)
        if intermediate_result.status:
            result = DB.delete("DELETE FROM IS601_MP3_Organizations WHERE id = %s", organization_id)

        # TODO delete-3 ensure a flash message shows for successful delete
        # rk868 11/27/23
        if result.status:
            flash("Deleted organization", "success")

    except Exception as e:
        print(f"{e}")
        flash("Error deleting organization", "danger")

    # TODO delete-4 pass all argument except id to this route
    # rk868 11/27/23
    args = request.args.copy()
    args.pop("id", None)

    # TODO delete-5 redirect to organization search
    # rk868 11/27/23
    return redirect(url_for("organization.search", **args))

