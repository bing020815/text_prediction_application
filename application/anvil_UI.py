from ._anvil_designer import Text_Prediction_HomeTemplate
from anvil import *
import anvil.server

class Text_Prediction_Home(Text_Prediction_HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.

  def timer_1_tick(self, **event_args):
    """This method is called Every [1] seconds. Does not trigger if [interval] is 0.5"""
    # When there is at least two words to trigger the prediction
    if len(self.text_area_review.text) >= 2:
      # get the full input
      text = self.text_area_review.text.lower()
      
      ## prediction for text and sentiment
      predicted_word, predicted_class = anvil.server.call_s('app_prediction', text)


      ## display text prediction
      if predicted_word is not None:  
        self.text_area_text_predicted.text= text + ' ' + predicted_word
        self.text_area_text_predicted.visible = True
        self.label_text_prediction.text = predicted_word
        self.label_text_prediction.visible = True
        self.label_text_prediction.bold = True
        self.label_text_prediction.align = 'center'
        self.label_recommend.visible = True
        self.label_preview.visible = True
        
       
      ## display sentiment prediction      
      if predicted_class==1:        # predicted as positive
          # word switches
        self.label_pos.font_size=26
        self.label_pos.foreground='#6118e7'
        self.label_pos.visible = True  # pos on
        self.label_neg.visible = False
          # emoji switches
        self.image_neu.visible = False
        self.image_pos.visible = True  # pos on
        self.image_neg.visible = False
        
      elif predicted_class==0:      # predicted as negative
          # word switches
        self.label_neg.font_size=26
        self.label_neg.foreground='#ff0000'
        self.label_pos.visible = False
        self.label_neg.visible = True  # neg on
          # emoji switches
        self.image_neu.visible = False
        self.image_pos.visible = False
        self.image_neg.visible = True  # neg on
      
      # if there is no input in the textbox
    else:
        self.label_pos.visible = False
        self.label_neg.visible = False
        self.image_neu.visible = True
        self.image_pos.visible = False
        self.image_neg.visible = False
        self.label_text_prediction.visible = False
        self.text_area_text_predicted.visible = False
        self.label_recommend.visible = False
        self.label_preview.visible = False
