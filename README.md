
# DoNation Technical Assignment

The Do Nation platform allows individuals to pledge to do an action to improve their lives
and make an environmental impact. Each action in our system is capable of supporting
multiple metrics, for example, CO2, water and waste. When a user pledges to do an action,
they answer a few questions which generate the savings expected if they do as promised.

# API Endpoints

## FETCH all user pledges

```
/api/fetch/<uid>
```

where `uid` is the user id you wish to fetch all the pledges for.

## POST a user pledge

```
/api/post/<uid>/<pledge>/<co2>
```

where `uid` is the user id <br/>
where `pledge` is the pledge you wish to post <br/>
and `co2` is the co2 saved by the pledge <br/>

## FETCH total CO2 saved

```
/api/total/co2
```

will return json object with `saved_co2__sum` as the key and `total co2` as the value.
