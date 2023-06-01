from .imports import *
from .preprocess import correct_line, strt_stp_pos_image, detect_horizontal_line
from .extract_date import ext_date
from .extract_amount import ext_amount
from .extract_ocr_details import ext_ocr_details
from .extract_MICR import extract_micr
import argparse
from pprint import pprint

import re


def cheque_ocr(image_path):

    # d={'PayeeName': 'PadabaD . Pradeep Kumar', 'AC/NO': '1130002010108841', 'IFSC': 'SYNB0003011', 'Amount': '8800000', 'Cheque MICR Number': 'DDD683651DDD 5666 D5633D 29666 2U'}
    # d.update({'signature':'/home/gaurav/FinalProject/apps/vision/ChequeOCR/feilds/signature.jpg'})
    # return d

    # parser = argparse.ArgumentParser()
    # parser.add_argument('--input_image', help="Path to cheque image")
    # args = parser.parse_args()
    img_color = cv2.imread(image_path)

    print(img_color)
    if img_color.ndim == 3:
        img = cv2.cvtColor(img_color, cv2.COLOR_RGB2GRAY)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)[1]
    # img = set_contrast(img)[0]                                     # set contrast
    cv2.imwrite('img_th2.jpg', img)
    # line_img = detect_horizontal_line(img)
    # cv2.imwrite('line_img.jpg', line_img)
    #img = detect_horizontal_line(img)
    print("correct line start")
    line_corrected_img, mask = correct_line(img)
    print("correct line end",line_corrected_img)
    cv2.imwrite('preprocessed_img3.jpg', line_corrected_img)
    print("image write done")




    # exit()
    extracted_micr = extract_micr(image=line_corrected_img)[0]
    # print('MICR->', extracted_micr)
    print("done extracted_micr", extracted_micr)
    date = ext_date(line_corrected_img, mask)  # extract date
    print("data is")
    # print(date)
    # print('date->', "".join(date))

    template = cv2.imread('/home/gaurav/FinalProject/apps/vision/ChequeOCR/rupee_template_2.jpg', 0)                 # rupee symbol template
    amount = ext_amount(line_corrected_img, template)

    #pay_template = cv2.imread('./Pay.jpg', 0)
    print(f'line corrected image is {line_corrected_img}')
    details = ext_ocr_details(line_corrected_img)
    detail = details[:-1]
    signature = details[-1]
    fields = ['PayeeName', 'AC/NO', 'IFSC']
    cheque_fields = {}
    for field,checK_field in zip(fields, detail):
        cheque_fields.update({field:checK_field})

    cheque_fields["AC/NO"]= re.sub("[^0-9]", "", cheque_fields["AC/NO"])

    amount=re.sub("[^0-9]", "", amount)

    cheque_fields.update({'Amount':amount})
    cheque_fields.update({'Cheque MICR Number':extracted_micr})
    cheque_fields.update({'signature':'/home/gaurav/FinalProject/apps/vision/ChequeOCR/feilds/signature.jpg'})
    print("cheque Field ",cheque_fields)



    return cheque_fields
    details_df = pd.DataFrame(cheque_fields, index=[0])

    pprint(details_df)
    print(type(details_df.index))
    # details_df['Signature'] = pd.Series(index=details_df.index,dtype='float64')  
    details_df['Signature'] =   '/home/gaurav/FinalProject/apps/vision/ChequeOCR/feilds/signature.jpg' 


    # print(details_df.head())

    writer = pd.ExcelWriter('/home/gaurav/FinalProject/apps/vision/ChequeOCR/Cheque_details.xlsx', engine='xlsxwriter')
    details_df.to_excel(writer, sheet_name='Sheet1')
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']

    # Insert an image.
    worksheet.insert_image('G2', '/home/gaurav/FinalProject/apps/vision/ChequeOCR/feilds/signature.jpg')

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()


    return details_df

