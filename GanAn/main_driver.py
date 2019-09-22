from common.message_handler import MessageHandlerService
from common.rabbitmq import RabbitMq
import logging
import json

from drf_yasg.utils import swagger_auto_schema

logger = logging.getLogger(__name__)


class Publish:

    def publish_(self, request, format=None):
        """
        This Post method will request for check  backup status for a  VM
        :param request: Request object
        :param format: Json
        :return: Json response
        """
        logger.info(" Inside: publish method")
        try:
            # Publish job to the message broker code goes here.
            input_dict = request.data
            client = MessageHandlerService(RabbitMq(QUEUE_NAME, BACKUP_ROUTING_KEY))
            client.handle_message(input_dict, BACKUP_CHECK_STATUS_METHOD)
            ret_dict = {"message": "Check backup status job initiated"}
            logger.info("{} Exit: post of check backup status".format(BACKUP_LOG_ID))
            return Response(ret_dict)
        except Exception as e:
            if hasattr(e, 'message'):
                err_msg = "Unable to initiate check backup status request due to {}".format(e.message)
            else:
                err_msg = "Unable to initiate check backup status request due to {}".format(e)
            logger.exception("{} Exception {}".format(BACKUP_LOG_ID, err_msg))
            content = {"Message": err_msg}
            return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
