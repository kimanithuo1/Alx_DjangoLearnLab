Introduction to Django -LibraryProject

# Advanced Features and Security

This Django project demonstrates:

1. **Custom User Model**  
   - Added `date_of_birth` and `profile_photo` fields.  
   - Configured `CustomUserManager` for user and superuser creation.  

2. **Permissions and Groups**  
   - Custom permissions (`can_add_book`, `can_change_book`, `can_delete_book`) defined in the `Book` model.  
   - Groups (`Editors`, `Viewers`, `Admins`) created and assigned permissions.  
   - Views protected with `@permission_required` decorators.  

3. **Security Best Practices**  
   - CSRF protection included in forms.  
   - HTTPS and secure cookie settings prepared in `settings.py`.  
   - Safe queries using Django ORM.  

📂 See [permissions_README.md](permissions_README.md) for detailed notes on permissions.
