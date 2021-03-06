from osv import osv
from osv import fields

class SWS_Criteria(osv.osv):
 
    _name = 'sws.criteria'
    _description = 'sws.criteria'
 
    _columns = {
            'name':fields.char('Criteria Name:', required=False),
            'criteria_no':fields.integer('Criteria Number:', required=False), 
            'active_is':fields.boolean('Active',required=False),
            'date_valid':fields.date('Date valid From',required=False),
            'criteria_line_id':fields.one2many('sws.criteria.line','criteria_id'),  
            
                }
SWS_Criteria()

class SWS_Criteria_line(osv.osv):
 
    _name = 'sws.criteria.line'
    _description = 'sws.criteria.line'
 
    _columns = {
            'category':fields.many2one('product.product','Category',domain=[('income','=',False),('expense','=',False)], required=True), 
            'lower_age':fields.integer('Lower Age Limit',required=False),
            'higher_income':fields.integer('higher Income Limit',required=False),
            'min_exp':fields.integer('Minimum Experience(in year)',required=False),
            'min_work_gap':fields.integer('Minimum Work Gap(in months)',required=False),
            'criteria_id':fields.many2one('sws.criteria','Category', required=False),   
            
                }
SWS_Criteria_line()