# nOSINTh
Norwegian Open Source Intelligence Harvester

This is a simple Python script that let's you search for a person or company.
The script searches the Norwgian postal database, phone register and national organizations register
and parses the results through lxml and request to be presented in a nice list.
The purpose is to be able to quickly establish if the persons name is correct, if there's more than one with
the same name, are they owners of an organization etc.
There's an option to open the search in a browser to see the complete results on the different source sites.
An additional option also searches WHOIS at Norid (requires CAPTCHA input) and Aksjonærregisteret (stock owners).

This is made for a school project. Programmed and tested in a Kali Linux 2018 Virtualbox. 
The code is little messy and there is no error handling, will fix this in a later version.

Version 1.0 is pretty simple, later versions should include much more information (like actual phone numbers
and addresses) and have more sources to search from.
