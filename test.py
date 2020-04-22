import os
import tensorflow as tf
import numpy as np
import cv2

LABELS_TXT_FILE = os.getcwd() + "/" + "trained_labels.txt"
GRAPH_PB_FILE = os.getcwd() + "/" + "trained_graph.pb"
TEST_IMAGES_DIR = os.getcwd() + "/static/img"

def mushroom():
    # Here I create an array to hold the labels of classifications
    # All the Genus Im using
    mushroomGenus = []
    for currentLine in tf.gfile.GFile(LABELS_TXT_FILE):
        classification = currentLine.rstrip()
        mushroomGenus.append(classification)

    # load the graph from file
    with tf.gfile.FastGFile(GRAPH_PB_FILE, 'rb') as retrainedGraphFile:
        graphDef = tf.GraphDef()
        graphDef.ParseFromString(retrainedGraphFile.read())
        _ = tf.import_graph_def(graphDef, name='')

    # This will make sure it is .jpg or .jpeg
    with tf.Session() as sess:
        for fileName in os.listdir(TEST_IMAGES_DIR):
            if not (fileName.lower().endswith(".jpg") or fileName.lower().endswith(".jpeg")):
                continue

            #Need file path for image and open with openCV
            imageFileWithPath = os.path.join(TEST_IMAGES_DIR, fileName)
            openCVImage = cv2.imread(imageFileWithPath)

            # if no image
            if openCVImage is None:
                continue


            # This gets tensor and converts our image to a tensorflow image
            # Get the classification & sort from most confidence to least
            getTensor = sess.graph.get_tensor_by_name('final_result:0')
            tfImage = np.array(openCVImage)[:, :, 0:3]
            classifiedMushrooms = sess.run(getTensor, {'DecodeJpeg:0': tfImage})
            sortedClassifications = classifiedMushrooms[0].argsort()[-len(classifiedMushrooms[0]):][::-1]


            onMostLikelyPrediction = True
            info=[]
            for classify in sortedClassifications:
                strClassification = mushroomGenus[classify]
                confidence = classifiedMushrooms[0][classify]
                if onMostLikelyPrediction:
                    scoreAsAPercent = confidence * 100.0
                    info.append("the object appears to be a " + strClassification + ", " + "{0:.2f}".format(scoreAsAPercent) + "% confidence")
                    cv2.imshow(fileName, openCVImage)
                    onMostLikelyPrediction = False
                info.append(strClassification + " (" +  "{0:.5f}".format(confidence) + ")")

            return info
