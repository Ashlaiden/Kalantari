

def get_user_IP(request):
    # Get the client's IP address from the request.META dictionary
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # If the 'HTTP_X_FORWARDED_FOR' header is present, the client's IP address is the first one in the list
        ip = x_forwarded_for.split(',')[0]
    else:
        # If the 'HTTP_X_FORWARDED_FOR' header is not present, use the 'REMOTE_ADDR' key
        ip = request.META.get('REMOTE_ADDR')
    return ip


# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]  # Use the first IP in the list
#     else:
#         ip = request.META.get('REMOTE_ADDR')  # Fallback to REMOTE_ADDR
#     return ip


