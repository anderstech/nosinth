# nosinth
Norwegian Open Source Intelligence Harvester

This is a super simple Python script that let's you search for a person or company.
The script then searches the Norwgian postal database, phone register and national organizations register
and parses the results through lxml and request to be presented in a nice list.
The purpose is to be able to quickly establish if the persons name is correct, if there's more than one with
the same name, are they owners of an organization etc.

This is made for a school project.

Version 1.1 is pretty simple, later versions should include much more information (like actual phone numbers
and addresses) and have more sources to search from.
