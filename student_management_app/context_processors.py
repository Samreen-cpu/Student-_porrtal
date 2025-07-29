# student_management_app/context_processors.py
# def user_role_processor(request):
#     user_role = None
#     if request.user.is_authenticated:
#         user_role = request.user.role
#     return {'user_role': user_role}
# student_management_app/context_processors.py
import logging

logger = logging.getLogger(__name__)

def user_role_processor(request):
    user_role = None
    if request.user.is_authenticated:
        user_role = getattr(request.user, 'role', 'Role_Attribute_Missing_In_Model')
        logger.info(f"Context Processor: User '{request.user.username}' is authenticated. Role found: '{user_role}'")
    else:
        logger.info("Context Processor: User is NOT authenticated.")
    return {'user_role': user_role}