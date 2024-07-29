from cloudflare import Cloudflare


# define your variable here

cloudflare_token = "your-cloudflare-token"
cloudflare_zone_id = "zone"
alias_name = "www.mydns.com"
cannonical_name = "cname.example.com"

# build cloudflare driver here
client = Cloudflare(api_token=cloudflare_token)



# create dns using defined driver
dns = client.dns.records.create(
    zone_id=cloudflare_zone_id, 
    type='CNAME', 
    name=alias_name, 
    content=cannonical_name,
    proxied=False
    )

# print output
print(dns)