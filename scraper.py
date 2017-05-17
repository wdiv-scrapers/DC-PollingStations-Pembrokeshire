from dc_base_scrapers.geojson_scraper import GeoJsonScraper


stations_url = "http://www.pembrokeshire.gov.uk/geoserver/maps/live/wms?service=WFS&version=1.3.0&request=GetFeature&typeNames=PCC%3AtblPollingStation&outputFormat=json&srsName=EPSG%3A4326"
districts_url = "http://www.pembrokeshire.gov.uk/geoserver/maps/live/wms?service=WFS&version=1.3.0&request=GetFeature&typeNames=PCC%3AtblPollingDistrict&outputFormat=json&srsName=EPSG%3A4326"
council_id = 'W06000009'


stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts')
districts_scraper.scrape()
