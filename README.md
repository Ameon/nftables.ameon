# nftables

Syntax highlighting for nftables configuration files in Visual Studio Code.

## Features

- Syntax highlighting for nftables configuration files
- Highlighting of tables, chains, sets, counters and rules
- Highlighting of IPv4 and IPv6 addresses
- Highlighting of protocols, actions and keywords
- Highlighting of object declarations and references
- Bracket matching and automatic closing
- Comment support
- Automatic indentation

## Supported files

- `.nft`

## Example

~~~nft
table inet preblock {
  set trusted_ipv4 {
    type ipv4_addr
    flags interval
  }

  chain prerouting {
    type filter hook prerouting priority raw; policy accept;

    ip saddr @trusted_ipv4 accept
  }
}
~~~

## Publisher

Ameon
