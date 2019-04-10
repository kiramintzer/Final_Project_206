from lyft_rides.auth import ClientCredentialGrant
from lyft_rides.session import Session

import lyft_tokens
import json
from lyft_rides.client import LyftRidesClient

auth_flow = ClientCredentialGrant(
    lyft_tokens.YOUR_CLIENT_ID,
    lyft_tokens.YOUR_CLIENT_SECRET,
    lyft_tokens.YOUR_PERMISSION_SCOPES,
    )
session = auth_flow.get_session()
client = LyftRidesClient(session)

response = client.get_cost_estimates(
    start_latitude = 37.7766,
    start_longitude = -122.391,
    end_latitude = 37.7972,
    end_longitude = -122.4533,
    ride_type = 'lyft'
)
estimate = response.json.get('cost_estimates')
distance = estimate[0]['estimated_distance_miles']
costmin = estimate[0]['estimated_cost_cents_min']
costmax = estimate[0]['estimated_cost_cents_max']

print(distance)
print(costmin)
print(costmax)

# for line in estimate:
#     print(line)
