from __future__ import division
import matplotlib.pyplot as plt
import numpy as np 
 
def cmdscale(D):
    """                                                                                       
    Classical multidimensional scaling (MDS)                                                  
                                                                                               
    Parameters                                                                                
    ----------                                                                                
    D : (n, n) array                                                                          
        Symmetric distance matrix.                                                            
                                                                                               
    Returns                                                                                   
    -------                                                                                   
    Y : (n, p) array                                                                          
        Configuration matrix. Each column represents a dimension. Only the                    
        p dimensions corresponding to positive eigenvalues of B are returned.                 
        Note that each dimension is only determined up to an overall sign,                    
        corresponding to a reflection.                                                        
                                                                                               
    e : (n,) array                                                                            
        Eigenvalues of B.                                                                     
                                                                                               
    """
    # Number of points                                                                        
    n = len(D)
    # Centering matrix                                                                        
    H = np.eye(n) - np.ones((n, n))/n
    # YY^T                                                                                    
    B = -H.dot(D**2).dot(H)/2
    # Diagonalize                                                                             
    evals, evecs = np.linalg.eigh(B)
    # Sort by eigenvalue in descending order                                                  
    idx   = np.argsort(evals)[::-1]
    evals = evals[idx]
    evecs = evecs[:,idx]
    # Compute the coordinates using positive-eigenvalued components only                      
    w, = np.where(evals > 0)
    L  = np.diag(np.sqrt(evals[w]))
    V  = evecs[:,w]
    Y  = V.dot(L)
    return Y, evals

def solve(str):
	plt.clf()
	plt.axis('equal')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title(str)
	cord = {}
	cord[str], _ = cmdscale(dis[str])
	cord[str] = cord[str][:, :2]
	cord[str][:, 0] = -cord[str][:, 0]
	theta = np.radians(-10)
	c, s = np.cos(theta), np.sin(theta)
	cord[str] = cord[str].dot(np.array([[c, -s], [s, c]]))
	plt.scatter(cord[str][:, 0], cord[str][:, 1])
	for i, city in enumerate(cities[str]):
		plt.annotate(city, xy = tuple(cord[str][i].tolist()), size=8)

	plt.savefig(str + '.png', dpi = 240)


cities = {}
dis = {}
cities['China'] = ['Beijing',  
	'Tianjin',  
	'Shanghai', 
	'Chongqing',
	'Hohhot',   
	'Urumqi',   
	'Lhasa',    
	'Yinchuan', 
	'Nanning',  
	'Harbin',   
	'Changchun',
	'Shenyang'
]
dis['China'] = np.array([
	[0,125,1239,3026,480,3300,3736,1192,2373,1230,979,684],
	[125,0,1150,1954,604,3330,3740,1316,2389,1207,955,661],
	[1239,1150,0,1945,1717,3929,4157,2092,1892,2342,2090,1796],
	[3026,1954,1945,0,1847,3202,2457,1570,993,3156,2905,2610],
	[480,604,1717,1847,0,2825,3260,716,2657,1710,1458,1164],
	[3300,3330,3929,3202,2825,0,2668,2111,4279,4531,4279,3985],
	[3736,3740,4157,2457,3260,2668,0,2547,3431,4967,4715,4421],
	[1192,1316,2092,1570,716,2111,2547,0,2673,2422,2170,1876],
	[2373,2389,1892,993,2657,4279,3431,2673,0,3592,3340,3046],
	[1230,1207,2342,3156,1710,4531,4967,2422,3592,0,256,546],
	[979,955,2090,2905,1458,4279,4715,2170,3340,256,0,294],
	[684,661,1796,2610,1164,3985,4421,1876,3046,546,294,0]
])

cities['America'] = [
	'Boston',         
	'Buffalo',        
	'Chicago',        
	'Dallas',         
	'Denver',         
	'Houston',        
	'Los Angeles',    
	'Memphis',        
	'Miami',          
	'Minneapolis',    
	'New York',       
	'Omaha',          
	'Philadelphia',   
	'Phoenix',        
	'Pittsburgh',     
	'Saint Louis',    
	'Salt Lake City', 
	'San Francisco',  
	'Seattle',        
	'Washington D.C.'
]

dis['America'] = np.array([
	[0,400,851,1551,1769,1605,2596,1137,1255,1123,188,1282,271,2300,483,1038,2099,2699,2493,393],
	[400,0,454,1198,1370,1286,2198,803,1181,731,292,883,279,1906,178,662,1699,2300,2117,292],
	[851,454,0,803,920,940,1745,482,1188,355,713,432,666,1453,410,262,1260,1858,1737,597],
	[1551,1198,803,0,663,225,1240,420,1111,862,1374,586,1299,887,1070,547,999,1483,1681,1185],
	[1769,1370,920,663,0,879,831,879,1726,700,1631,488,1579,586,1320,796,371,949,1021,1494],
	[1605,1286,940,225,879,0,1374,484,968,1056,1420,794,1341,1017,1137,679,1200,1645,1891,1220],
	[2596,2198,1745,1240,831,1374,0,1603,2339,1524,2451,1315,2394,357,2136,1589,579,347,959,2300],
	[1137,803,482,420,879,484,1603,0,872,699,957,529,881,1263,660,240,1250,1802,1867,765],
	[1255,1181,1188,1111,1726,968,2339,872,0,1511,1092,1397,1019,1982,1010,1061,2089,2594,2734,923],
	[1123,731,355,862,700,1056,1524,699,1511,0,1018,290,985,1280,743,466,987,1584,1395,934],
	[188,292,713,1374,1631,1420,2451,957,1092,1018,0,1144,83,2145,317,875,1972,2571,2408,230],
	[1282,883,432,586,488,794,1315,529,1397,290,1144,0,1094,1036,836,354,833,1429,1369,1014],
	[271,279,666,1299,1579,1341,2394,881,1019,985,83,1094,0,2083,259,811,1925,2523,2380,123],
	[2300,1906,1453,887,586,1017,357,1263,1982,1280,2145,1036,2083,0,1828,1272,504,653,1114,1973],
	[483,178,410,1070,1320,1137,2136,660,1010,743,317,836,259,1828,0,559,1668,2264,2138,192],
	[1038,662,262,547,796,679,1589,240,1061,466,875,354,811,1272,559,0,1162,1744,1724,712],
	[2099,1699,1260,999,371,1200,579,1250,2089,987,1972,833,1925,504,1668,1162,0,600,701,1848],
	[2699,2300,1858,1483,949,1645,347,1802,2594,1584,2571,1429,2523,653,2264,1744,600,0,678,2442],
	[2493,2117,1737,1681,1021,1891,959,1867,2734,1395,2408,1369,2380,1114,2138,1724,701,678,0,2329],
	[393,292,597,1185,1494,1220,2300,765,923,934,230,1014,123,1973,192,712,1848,2442,2329,0]
])

solve('China')
solve('America')