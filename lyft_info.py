from lyft_rides.auth import ClientCredentialGrant
from lyft_rides.session import Session

import lyft_tokens
import json


auth_flow = ClientCredentialGrant(
    lyft_tokens.YOUR_CLIENT_ID,
    lyft_tokens.YOUR_CLIENT_SECRET,
    lyft_tokens.YOUR_PERMISSION_SCOPES,
    )
session = auth_flow.get_session()

from lyft_rides.client import LyftRidesClient
client = LyftRidesClient(session)
response = client.get_cost_estimates(37.7763, -122.391, 37.7972, -122.4533)
ride_types = response.json.get('cost_estimates')
print(ride_types)