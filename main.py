import gpxpy
import gpxpy.gpx
import numpy as np
from sklearn.cluster import DBSCAN

def read_gpx(file_path):

	gpx_file = open(file_path, 'r')
	gpx = gpxpy.parse(gpx_file)

	return gpx

def export_data(gpx):
    
	lol=[]
	for track in gpx.tracks:
		for segment in track.segments:
			for point in segment.points:
# 				print('Point at ({0},{1}) -> {2}'.format(
# 					point.latitude,
# 					point.longitude,
# 					point.elevation))
				lol.append([
					point.latitude,
					point.longitude])
	return np.array(lol)

def build_cluster(geo_array, epsilon, min_points):
	clustering = DBSCAN(
		eps=epsilon/6371,
		min_samples=min_points,
		algorithm='ball_tree',
		metric='haversine').fit(geo_array)
	unique, counts = np.unique(clustering.labels_, return_counts=True)
	print(np.asarray((unique, counts)).T)
	labels = np.reshape(clustering.labels_,(len(clustering.labels_),1))
	new_array = np.concatenate((geo_array, labels), axis=1)
	return clustering, new_array, labels


if __name__ == "__main__":

	gpx = read_gpx('data/Massive_GPS_noise_will_fix_it_later.gpx')
	geo_array = export_data(gpx)
	c, a = build_cluster(geo_array, 1, 10)
