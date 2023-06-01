from .imports import *
  
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/home/gaurav/FinalProject/apps/vision/ChequeOCR/scripts/fluent-archway-385107-7d396346cbba.json'
import json
def vision_api(f,image_context=''):

	client = vision.ImageAnnotatorClient() 
	# f = 'amount_img.jpg'
	with io.open(f, 'rb') as image: 
	    content = image.read()
	print("whats the issue",content)
	image = vision.Image(content = content)
	# image = visi

	if image_context == 'bearer':
		handwritten_image_context = vision.ImageContext(language_hints=['en-t-i0-handwrit'])
		response = client.document_text_detection(image=image, image_context=handwritten_image_context)
	else:
		response = client.document_text_detection(image = image)
	  
	a = plt.imread(f)
	plt.imshow(a)
	  
	txt = []
	para=[]
	# out_file = open("block.json", "w")
	# outdile= open('out.txt', 'w')
    # print('Filename:', filename, file=f) 
	
	for page in response.full_text_annotation.pages:
		for block in page.blocks: 
	        # print('\nConfidence: {}%\n'.format(block.confidence * 100)) 
			for paragraph in block.paragraphs:
				# para.append(paragraph)
				print(paragraph)

				for word in paragraph.words: 
					word_text = ''.join([symbol.text for symbol in word.symbols]);print("word text is",word_text)
					txt.append(word_text) 
				if image_context=="bearer":
					break
			if image_context=="bearer":
					break
	# json.dump(para, out_file, indent = 6)
  
	# outdile.close()					
					
	return txt

if __name__ == "__main__":
	print("text is ",vision_api('./../feilds/payee.jpg','bearer'))