# product-api
Product API endpoint implemented using Django &amp; Django REST Framework

## Setting up the Database
<pre>
    #### Execute Commands
        - Activate the virtualenv
            -  macOS (source bin/activate) & windows (Scripts\bin\activate)
            -  pip install -r requirements.txt
            -  python manage.py makemigrations
            -  python manage.py migrate
</pre>

## API Endpoint
 - api/product/{product-name} (get request)
 - api/serach (post request : input : product_name)
