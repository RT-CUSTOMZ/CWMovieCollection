#!/usr/bin/python

from CWMovieCollectionLoadSaveManager import CWMovieCollectionLoadSaveManager
from CWMovieCollectionParsingManager import CWMovieCollectionParsingManager

LoadSaveManager = CWMovieCollectionLoadSaveManager()
ParsingManager = CWMovieCollectionParsingManager()

#MovieCollection = []

#dvd = ParsingManager.Parse('4010232049841')
#MovieCollection.append(dvd)

#MovieCollection.append(dvd)

#LoadSaveManager.SaveMovieCollection(MovieCollection)
MovieCollection = LoadSaveManager.LoadMovieCollection()

for item in MovieCollection:
	print item.title

'''if MovieCollection != None:
	dvd = MovieCollection

	print dvd	

	print dvd.title
	print dvd.price
	print dvd.directors
	print dvd.actors
	print dvd.productGroup
	print dvd.manufacturer
	print dvd.amazonUrl
	print dvd.asin
	print dvd.studio
	print dvd.audienceRating
	print dvd.imageUrl
	print dvd.summary
	print dvd.languages
	print dvd.subtitles
	print dvd.audioFormats
	print dvd.publicationDate
	print dvd.runningTime'''

#item = api.item_lookup(ItemId='', IdType='EAN', SearchIndex='All', ResponseGroup='Large').Items.Item

#ASIN = item.ASIN
#print ASIN

#for act in item.ItemAttributes.Actor:
#	try:
#		print act
#	except:
#		print 'Error'


#print item.LargeImage.URL

#print item.Offers.Offer.OfferListing.Price.FormattedPrice