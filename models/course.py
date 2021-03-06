# -*- coding: utf-8 -*-
from odoo  import api, fields, models , exceptions

class CustomPopMessage(models.TransientModel):
    _name = "custom.pop.message"
    name = fields.Char('Message')


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Course'

    name = fields.Char(string='Title', required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('openacademy.partner', string="Responsible")
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")

    level = fields.Selection([('1', 'Easy'), ('2', 'Medium'), ('3', 'Hard')], string="Difficulty Level")



class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Session'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    state = fields.Selection([('draft', "Draft"), ('confirmed', "Confirmed"), ('done', "Done")], default='draft')

    start_date = fields.Date(default=fields.Date.context_today)
    duration = fields.Float(digits=(6, 2), help="Duration in days", default=1)

    instructor_id = fields.Many2one('openacademy.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('openacademy.partner', string="Attendees" )

    seats_available = fields.Integer("Seats Available")

    _sql_constraints = [

        ('_onchange_attendee_ids', '(len(attendee_ids)>seats_available)', 'Location ID must be unique !'),

    ]


    @api.onchange('attendee_ids')
    def _onchange_attendee_ids(self):
      for record in self:
        if len(self.attendee_ids) > self.seats_available:
            # raise Warning(("filled"))
            return {'value': {}, 'warning': {'title': 'Warning', 'message': 'Sheats Filled'}}













