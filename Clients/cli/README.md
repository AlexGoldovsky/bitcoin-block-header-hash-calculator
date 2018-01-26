# BlockHeaderHash CLI Client

## Run an Example
```PYTHONPATH=. python Clients/cli/cli-client.py example```

The output should be as follows:
```
Calculating Block Header Hash for the following values:
Version - 3
Previous Block Hash - 0000000000000000051f5de334085b92ce27c03888c726c9b2bb78069e55aeb6
Merkle Root - f4db18d3ecab87eeb23a56490d5b0b514848d510d409b43f6bbf2b82f55da8db
Time - 1442663985
Bits - 403867578
Nonce - 3548193207
The Hash is 00000000000000000be983a81043933c38008010b849fd6a35d5dd2d57f929bd
```


## Hash by block header values
Here you have a couple of choices:

1. passing the block header properties as arguments: 
```
PYTHONPATH=. python Clients/cli/cli-client.py hash --version 3 --pbh 0000000000000000051f5de334085b92ce27c03888c726c9b2bb78069e55aeb6 --mr f4db18d3ecab87eeb23a56490d5b0b514848d510d409b43f6bbf2b82f55da8db --time 1442663985 --bits 403867578 --nonce 3548193207
```

2. Get prompted for each of the values:
```
PYTHONPATH=. python Clients/cli/cli-client.py hash
```

The output for both would be solely the hash value: `00000000000000000be983a81043933c38008010b849fd6a35d5dd2d57f929bd`

If you would like a more verbose output like in the example, add the --verbose flag to the command you run (prompted or not)

e.g - `PYTHONPATH=. python Clients/cli/cli-client.py hash --verbose`
after you would enter the values you're being prompt to enter you would get an out put similar to this:
```
Calculating Block Header Hash for the following values:
Version - 3
Previous Block Hash - 0000000000000000051f5de334085b92ce27c03888c726c9b2bb78069e55aeb6
Merkle Root - f4db18d3ecab87eeb23a56490d5b0b514848d510d409b43f6bbf2b82f55da8db
Time - 1442663985
Bits - 403867578
Nonce - 3548193207
The Hash is 00000000000000000be983a81043933c38008010b849fd6a35d5dd2d57f929bd
```

