from uber_rides.session import Session
from uber_rides.client import UberRidesClient

import uber_tokens
import json

session = Session(server_token= uber_tokens.server_token)
client = UberRidesClient(session)


response = client.get_price_estimates(
    start_latitude=37.770,
    start_longitude=-122.411,
    end_latitude=37.791,
    end_longitude=-122.405,
    seat_count=2
)

estimate = response.json.get('prices')
print(estimate)

# from uber_rides.auth import AuthorizationCodeGrant
# auth_flow = AuthorizationCodeGrant(
#     <CLIENT_ID>,
#     <SCOPES>,
#     <CLIENT_SECRET>,
#     <REDIRECT_URI>
# )
# auth_url = auth_flow.get_authorization_url()

# session = auth_flow.get_session(redirect_url)
# client = UberRidesClient(session, sandbox_mode=True)
# credentials = session.oauth2credential

