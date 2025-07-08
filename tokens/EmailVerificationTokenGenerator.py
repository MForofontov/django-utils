from django.core.signing import TimestampSigner, SignatureExpired, BadSignature
from django.conf import settings


class EmailVerificationTokenGenerator:
    """
    Class to generate and verify email verification tokens.
    """

    def __init__(self):
        self.secret_key = settings.SECRET_KEY
        self.signer = TimestampSigner(self.secret_key)

    def make_token(self, user):
        """
        Generate a token for the user.

        Parameters
        ----------
        user : CustomUser
            The user for whom the token is being generated.

        Returns
        -------
        str
            A string representing the token.
        """
        return self.signer.sign(user.pk)

    def check_token(self, token, max_age=86400):
        """
        Check if the token is valid and not expired.

        Parameters
        ----------
        token : str
            The token to check.
        max_age : int
            The maximum age of the token in seconds (default is 1 day).

        Returns
        -------
        int or str
            The user_id if the token is valid and not expired, 'expired' if the token is expired,
            'invalid' if the token is invalid.
        """
        try:
            user_id = self.signer.unsign(token, max_age=max_age)
            return int(user_id)
        except SignatureExpired:
            # Token is valid but expired
            return "expired"
        except BadSignature:
            # Token is invalid
            return "invalid"


# Create an instance of the EmailVerificationTokenGenerator
email_verification_token = EmailVerificationTokenGenerator()
