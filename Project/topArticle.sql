SELECT ActionGeo_CountryCode , SUM(NumArticles) AS Sum_Articles
FROM [gdelt-bq:full.events] 
WHERE Year >1999 and Year < 2017 and(EventRootCode == "18" or EventRootCode == "19" or EventRootCode == "20") and ActionGeo_CountryCode is not null
GROUP BY ActionGeo_CountryCode 
ORDER BY Sum_Articles desc