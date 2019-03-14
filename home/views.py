import requests

from rest_framework.views import APIView
from rest_framework.response import Response

BASE_URL = 'http://metadata.google.internal/computeMetadata/v1/'


class ViewVersion(APIView):

    def get(self, request):
        try:
            return Response({
                'id': self._get_metadata('instance/id/'),
                'name': self._get_metadata('instance/name/'),
                'zone': self._get_metadata('instance/zone/')
            })
        except requests.exceptions.RequestException:
            return Response('Server connection error')
        except requests.exceptions.HTTPError:
            return Response('Data not available')

    def _get_metadata(self, attribute):
        url = '{}{}'.format(BASE_URL, attribute)
        response = requests.get(url)
        response.raise_for_status()

        return response.content
