# Inventory Management Application

This web application is designed to help manage inventory for any type of store. 

To test use the app, simply visit https://inventory-management.mattambrogi.repl.co/. 

To visit the replit code, visit https://replit.com/@mattambrogi/inventory-management

## User guide
The home page of the application contains a user guide. 

In short:
- Users can create products for their store to carry
- Users can create locations, which may represent warehouses or stores depending on the use case
- Users can then assign stock (a given quantity of any product) to locations

Users can view and manage inventory by
- Viewing all products
- Viewing all locations
- Viewing all stock across locations
- Viewing all products at a given location
- Viewing all locations where a given product is in stock

Within each of these views, users have the ability to create, update, and delete stock.

## Technical implementation

This project was built as a monolithic Django app, which lends itself particulary well to CRUD based applications.

URLs and Views map to the user screens mentioned above.

The database consistens of 3 models

**Product**: brand, item_name, price

**Location**: name, zip_code

**Stock**: product, location, quantity


## Further work

There are many features which could be added to this project given more time. To list a few:

- Add form validation to ensure consistency of all input data
- Add unique identifiers for products and locations instead of depending on primary keys
- Allow users to increment stock directly directly from lists instead of having to click into a separate page
- Build out more tests for reliability

