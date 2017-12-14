# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class InitialTwinProperties(Model):
    """InitialTwinProperties.

    :param desired: Gets and sets the InitialTwin desired properties.
    :type desired: ~service.models.TwinCollection
    """

    _attribute_map = {
        'desired': {'key': 'desired', 'type': 'TwinCollection'},
    }

    def __init__(self, desired=None):
        self.desired = desired
