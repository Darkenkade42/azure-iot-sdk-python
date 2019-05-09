# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from azure.iot.device.common.transport.pipeline_events_base import PipelineEvent


class C2DMessage(PipelineEvent):
    """
    A PipelineEvent object which represents an incoming C2D event.  This object is probably
    created by some converter stage based on a transport-specific event
    """

    def __init__(self, message):
        """
        Initializer for C2DMessage objects.

        :param Message message: The Message object for the message that was received.
        """
        super(C2DMessage, self).__init__()
        self.message = message


class InputMessage(PipelineEvent):
    """
    A PipelineEvent object which represents an incoming InputMessage event.  This object is probably
    created by some converter stage based on a transport-specific event
    """

    def __init__(self, input_name, message):
        """
        Initializer for InputMessage objects.

        :param str input_name: The name of the input that this message arrived on.  This string is
          also stored in the input_name attribute on the message object
        :param Message message: The Message object for the message that was received.
        """
        super(InputMessage, self).__init__()
        self.input_name = input_name
        self.message = message