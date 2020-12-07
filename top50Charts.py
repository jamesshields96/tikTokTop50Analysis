from fycharts.SpotifyCharts import SpotifyCharts

fyApi = SpotifyCharts()

fyApi.viral50Daily(output_file = "viral_50_daily.csv", start = "2020-11-01", end = "2020-12-01", region = 'us')


