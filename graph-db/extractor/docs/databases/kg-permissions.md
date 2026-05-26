# Set up database permissions

Run cypher-shell:
```
show databases; 
show users;

GRANT ALL GRAPH PRIVILEGES ON GRAPH `ecocyc-plus` TO humemycelium;
GRANT ACCESS ON DATABASE `ecocyc-plus` TO humemycelium;
GRANT CREATE NEW RELATIONSHIP TYPE ON DATABASE `ecocyc-plus` TO humemycelium;
GRANT CREATE NEW PROPERTY NAME ON DATABASE `ecocyc-plus` TO humemycelium;
GRANT CREATE NEW NODE LABEL ON DATABASE `ecocyc-plus` TO humemycelium;


GRANT ALL GRAPH PRIVILEGES ON GRAPH `ecocyc-mod` TO humemycelium;
GRANT ACCESS ON DATABASE `ecocyc-mod` TO humemycelium;
GRANT CREATE NEW RELATIONSHIP TYPE ON DATABASE `ecocyc-mod` TO humemycelium;
GRANT CREATE NEW PROPERTY NAME ON DATABASE `ecocyc-mod` TO humemycelium;
GRANT CREATE NEW NODE LABEL ON DATABASE `ecocyc-mod` TO humemycelium;
```


