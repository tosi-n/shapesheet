from .model import ClassificationModel
from scipy.special import softmax
import numpy as np
from tqdm import tqdm
tqdm.pandas()



base_model = './models'

model = ClassificationModel('bert', base_model, num_labels=2, use_cuda=False)#, args={'reprocess_input_data': True, 'overwrite_output_dir': True})

label_dict = {
        0:'non_title',
        1:'title'
        }



# Model fn_type inference and confidence score
def predict(Text, IsBold, IsItalic, IsUnderlined, Left, Right, Top, Bottom, FontType):
	content = [Text + ' ' + str(IsBold) + ' ' + str(IsItalic) + ' ' + str(IsUnderlined) + ' ' + str(Left) + ' ' + str(Right) + ' ' + str(Top) + ' ' + str(Bottom) + ' ' + FontType]
	preds_l, outputs = model.predict(content)

	confidence = []
	probabilities = np.array([softmax(element) for element in outputs])
	for i in probabilities:
		long_probs = np.amax(i)
		confidence.append(long_probs)

	for k, v in label_dict.items():
		if preds_l[0] == k:
			i = v
			# print(v)
				# return i

	return i, str(confidence[0])


# predict('Sales and Marketing', True, False, False, 33.1, 101.3, 66.6, 72.1, 'New Times Roman')