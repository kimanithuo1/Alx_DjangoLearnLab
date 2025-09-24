### API Endpoints
- GET /api/books/ → List all books
- POST /api/books/ → Create a new book (auth required)
- GET /api/books/{id}/ → Retrieve single book
- PUT/PATCH /api/books/{id}/ → Update a book (auth required)
- DELETE /api/books/{id}/ → Delete a book (auth required)





### Filtering
GET /api/books/?title=Things Fall Apart
GET /api/books/?publication_year=1958
GET /api/books/?author=1

### Searching
GET /api/books/?search=Yellow
GET /api/books/?search=Achebe

### Ordering
GET /api/books/?ordering=publication_year
GET /api/books/?ordering=-publication_year
GET /api/books/?ordering=title
