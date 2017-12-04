# my_project_1
Learn Django and Panda framework : Notes

Virtual Environment:
(myprojects) mmRbA:myprojects mayurinisar$ workon myprojects

Django Project: 
(myprojects) mmRbA:myprojects mayurinisar$ django-admin.py startproject myproject

High level Directory Structure:
The django-admin tool creates a folder/file structure as shown below:

	locallibrary/
	    manage.py
	    locallibrary/
		settings.py
		urls.py
		wsgi.py

The locallibrary project sub-folder is the entry point for the website: 

	•	*settings.py* contains all the website settings. This is where we register any applications we create, the location of our static files, database configuration details, etc.  
	
	•	*urls.py* defines the site url-to-view mappings. While this could contain all the url mapping code, it is more common to delegate some of the mapping to particular applications, as you'll see later.
	
	•	*wsgi.py* is used to help your Django application communicate with the web server. You can treat this as boilerplate.
	
The manage.py script is used to create applications, work with databases, and start the development web server. 

Django App: 
(myprojects) mmRbA:myprojects mayurinisar$ python manage.py startapp firstapp

Database settings: 

	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'myproject',
		'USER': 'myprojectuser',
		'PASSWORD': 'password',
		'HOST': 'localhost',
		'PORT': '',
	    }
	}

How to Access psql: 

(myprojects) mmRbA:myprojects mayurinisar$ workon myprojects
(myprojects) mmRbA:myprojects mayurinisar$ psql myproject


	myproject=# \dt
			      List of relations
	 Schema |            Name            | Type  |     Owner     
	--------+----------------------------+-------+---------------
	 public | auth_group                 | table | myprojectuser
	 public | auth_group_permissions     | table | myprojectuser
	 public | auth_permission            | table | myprojectuser
	 public | auth_user                  | table | myprojectuser
	 public | auth_user_groups           | table | myprojectuser
	 public | auth_user_user_permissions | table | myprojectuser
	 public | django_admin_log           | table | myprojectuser
	 public | django_content_type        | table | myprojectuser
	 public | django_migrations          | table | myprojectuser
	 public | django_session             | table | myprojectuser


Troubleshoot sql connection issues:

1 Error: 
(myprojects) mmRbA:myprojects mayurinisar$ psql myproject
psql: could not connect to server: No such file or directory
	Is the server running locally and accepting
	connections on Unix domain socket “/tmp/.s.PGSQL.5432"?

Solution: 

	postgres -D /usr/local/var/postgres
	rm -rf /usr/local/var/postgres && initdb /usr/local/var/postgres -E utf8
	pg_ctl -D /usr/local/var/postgres -l logfile start


What does the above command do?
1. It will give you a much more verbose output if postgres fails to start.
2.  a pid file was blocking postgres from starting up.
3.  start the server

2  What version of sql?
	psql myproject
	myproject=# SELECT version(); 


STEPS/NOTES:

1. To include the app in our project, we need to add a reference to its configuration class in the INSTALLED_APPS setting. The App_NameConfig class is in the app_name/apps.py file, so its dotted path is ‘app_name.apps. App_NameConfig'. Edit the project_name/settings.py file and add that dotted path to the INSTALLED_APPS setting.

If you make any changes in the models you need to run another command: 
Python manage.py makemigrations  app_name

By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

2. You can also run python manage.py check; this checks for any problems in your project without making migrations or touching the database.

3. Now, run migrate again to create those model tables in your database.
python manage.py migrate

The migrate command takes all the migrations that haven’t been applied (Django tracks which ones are applied using a special table in your database called django_migrations) and runs them against your database - essentially, synchronizing the changes you made to your models with the schema in the database.

4. Remember the three-step guide to making model changes:
	•	Change your models (in models.py).
	•	Run python manage.py makemigrations to create migrations for those changes
	•	Run python manage.py migrate to apply those changes to the database.

Questions: 
1. what does on_delete do on Django models? What does models.CASCADE do? What other options are available?

This is the behavior to adopt when the referenced object is deleted. It is not specific to Django, this is an SQL standard.
There are 6 possible actions to take when such event occurs:
	•	CASCADE: When the referenced object is deleted, also delete the objects that have references to it (When you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.
	•	PROTECT: Forbid the deletion of the referenced object. To delete it you will have to delete all objects that reference it manually. SQL equivalent: RESTRICT.
	•	SET_NULL: Set the reference to NULL (requires the field to be nullable). For instance, when you delete a User, you might want to keep the comments he posted on blog posts, but say it was posted by an anonymous (or deleted) user. SQL equivalent: SET NULL.
	•	SET_DEFAULT: Set the default value. SQL equivalent: SET DEFAULT.
	•	SET(...): Set a given value. This one is not part of the SQL standard and is entirely handled by Django.
	•	DO_NOTHING: Probably a very bad idea since this would create integrity issues in your database (referencing an object that actually doesn't exist). SQL equivalent: NO ACTION.
Source: Django documentation
See also the documentation of PostGreSQL for instance.
In most cases, CASCADE is the expected behaviour, but for every ForeignKey, you should always ask yourself what is the expected behaviour in this situation. PROTECT and SET_NULL are often useful. Setting CASCADE where it should not, can potentially delete all your database in cascade, by simply deleting a single user.


2. What are double underscores used for?

Field lookups
Field lookups are how you specify the meat of an SQL WHERE clause. They’re specified as keyword arguments to the QuerySetmethods filter(), exclude() and get().
Basic lookups keyword arguments take the form field__lookuptype=value. (That’s a double-underscore). For example:

	>>> Entry.objects.filter(pub_date__lte='2006-01-01')
	
translates (roughly) into the following SQL:

	SELECT * FROM blog_entry WHERE pub_date <= '2006-01-01';

The field specified in a lookup has to be the name of a model field. There’s one exception though, in case of a ForeignKey you can specify the field name suffixed with _id. In this case, the value parameter is expected to contain the raw value of the foreign model’s primary key. For example:

	>>> Entry.objects.filter(blog_id=4)


Example : year
For date and datetime fields, an exact year match. Allows chaining additional field lookups. Takes an integer year.
Example:

	Entry.objects.filter(pub_date__year=2005)
	Entry.objects.filter(pub_date__year__gte=2005)

SQL equivalent:

	SELECT ... WHERE pub_date BETWEEN '2005-01-01' AND '2005-12-31';
	SELECT ... WHERE pub_date >= '2005-01-01';


regex
Case-sensitive regular expression match.
The regular expression syntax is that of the database backend in use. In the case of SQLite, which has no built in regular expression support, this feature is provided by a (Python) user-defined REGEXP function, and the regular expression syntax is therefore that of Python’s re module.
Example:

	Entry.objects.get(title__regex=r'^(An?|The) +’)

SQL equivalents:

	SELECT ... WHERE title REGEXP BINARY '^(An?|The) +'; -- MySQL
	SELECT ... WHERE REGEXP_LIKE(title, '^(An?|The) +', 'c'); -- Oracle
	SELECT ... WHERE title ~ '^(An?|The) +'; -- PostgreSQL
	SELECT ... WHERE title REGEXP '^(An?|The) +'; -- SQLite
	
Using raw strings (e.g., r'foo' instead of 'foo') for passing in the regular expression syntax is recommended.

