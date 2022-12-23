from core.encryption import TokenEncrypter

class DecryptTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.token_encrypter = TokenEncrypter()

    def __call__(self, request):
        if "HTTP_AUTHORIZATION" in request.META:
            token_decrypted = self.token_encrypter.decrypt_user_token(encrypted_token=request.META["HTTP_AUTHORIZATION"])
            if 'error' in token_decrypted:
                del request.META["HTTP_AUTHORIZATION"]
            else:
                request.META["HTTP_AUTHORIZATION"] = token_decrypted["token"]
                print(request.META["HTTP_AUTHORIZATION"])
        response = self.get_response(request)
        return response
