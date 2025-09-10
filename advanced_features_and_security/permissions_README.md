# Permissions and Groups Setup

This document explains how custom permissions and groups are configured in the project, how to use them in views, and how to test them.

---

## Custom Permissions

In `relationship_app/models.py` (inside the `Book` model), the following custom permissions were created:

- `can_add_book` → Allows adding new books.  
- `can_change_book` → Allows editing existing books.  
- `can_delete_book` → Allows deleting books.  

---

## Creating Groups and Assigning Permissions

We created groups and assigned the above permissions using a management command or script named `create_groups.py`.  

Example setup:

- **Editors** → `can_add_book`, `can_change_book`  
- **Viewers** → (read-only access)  
- **Admins** → All permissions (`can_add_book`, `can_change_book`, `can_delete_book`)  

Run the group creation script:

```bash
python manage.py shell < create_groups.py
