# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class X509Certificates(Model):
    """Primary and secondary certificates.

    :param primary:
    :type primary: ~service.models.X509CertificateWithInfo
    :param secondary:
    :type secondary: ~service.models.X509CertificateWithInfo
    """

    _attribute_map = {
        'primary': {'key': 'primary', 'type': 'X509CertificateWithInfo'},
        'secondary': {'key': 'secondary', 'type': 'X509CertificateWithInfo'},
    }

    def __init__(self, primary=None, secondary=None):
        self.primary = primary
        self.secondary = secondary
