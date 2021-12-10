Notes -----------------------------------------------------------------
Some stops may have null entires in their columns.
E.g. sometimes this corresponds to a stop outside of Allegheny County.
E.g. sometimes this corresponds to lack of data (see region_id)

Columns Description ---------------------------------------------------
stop_id: is the stop_id from gtfs data.
census_block_geoid: is the geoid for the census block in which the stop
        is contained. Sometimes this is null (e.g. stops outside of Alleg. County).
zipcode: is the zipcode (postal code) in which the stop is contained.
        Sometimes this is null (e.g. stops outside of Alleg. County).
regiond_id: a unique identifier for the region in which the stop is contained.
        Sometimes this is null. (e.g. the region in which the stop
        is contained is not a recognized Zillow region. For example, most 
        recognized Zillow regions in Alleg. County are within the municipality
        of Pittsburgh (city). See .pdf images ZillowPa... and ZillowPittsburgh...
        for visualization of absent neigborhoods. The neighborhoods not absent are 
        in solid black).
region_name: A descriptor corresponding to the region_id. This is null
        whenever region_id is null.