# TODO
- [ ] explore writing in a compiled language (faster)
- [x] abstract code into multiple files
- [x] add classes
- [s] add server to allow for post requests to send emails (future use)
- [ ] (thoughts) send emails in isolation? i.e. users do not see who else got an email
- [x] add database table for cabinet members 
- [ ] expand server to send selective emails
- [x] creat git hook to update req.txt whenever env changes
- [x] refactor email_client to allow for null body 
- [x] Database.get should only return preferred email
- [x] Create wrapper function that sends emails via arguements
- [x] Create simple way to store and update email body, subject and candidates 
- [x] Write tests
- [x] Fix cascade of deletes and updates. Requires implementation of foreign keys for cabinet and blacklist tables
- [ ] add project to the byte ccny website project db
- [ ] expand current db to fall 2024 applicants

## Jawad
- [x] test the delete operation (why is it not working)
- [x] add current alumni to db
- [x] add blacklist to db 

## Fahad
- [x] CLI arguments
    - [x] subject taken from CLI 
- [x] add the HTML functionality (grab the body.html file as the main body)
- [x] update readme
- [ ] expand tests
- [ ] fix github action
- [ ] add database function to mark everyone/ specific persion as inactive
