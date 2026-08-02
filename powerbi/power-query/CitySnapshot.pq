let
    Source = Csv.Document(
        File.Contents(DataRoot & "/city_hourly.csv"),
        [Delimiter = ",", Columns = 12, Encoding = 65001, QuoteStyle = QuoteStyle.Csv]
    ),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars = true]),
    TypedColumns = Table.TransformColumnTypes(
        PromotedHeaders,
        {
            {"observed_at_utc", type datetimezone},
            {"city", type text},
            {"latitude", type number},
            {"longitude", type number},
            {"temperature_c", type number},
            {"apparent_temperature_c", type number},
            {"precipitation_probability_pct", Int64.Type},
            {"wind_speed_kmh", type number},
            {"pm10", type number},
            {"pm2_5", type number},
            {"european_aqi", Int64.Type},
            {"chaos_score", type number}
        }
    )
in
    TypedColumns

