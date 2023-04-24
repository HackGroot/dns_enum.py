import dns.resolver
import sys

def dns_enumeration(domain, record_type):
    try:
        result = dns.resolver.resolve(domain, record_type)
        for rdata in result:
            print(f"{record_type} record for {domain}: {rdata}")
    except dns.resolver.NoAnswer:
        print(f"No {record_type} record found for {domain}")
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <domain>")
        sys.exit(1)

    domain = sys.argv[1]

    # Common DNS record types for enumeration
    record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]

    for record_type in record_types:
        dns_enumeration(domain, record_type)

