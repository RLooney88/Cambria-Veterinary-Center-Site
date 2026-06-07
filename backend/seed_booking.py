"""Cambria-specific booking seed data. Idempotent on startup."""
from __future__ import annotations

import logging
from sqlalchemy import select

from database import AsyncSessionLocal
from models import AppointmentType, ClinicHours, StaffConfig

logger = logging.getLogger(__name__)

APPOINTMENT_TYPES = [
    {"name": "Wellness Exam", "description": "Routine wellness visit, preventive care, and vaccines for established or new patients.", "duration_mins": 30, "doctor_mins": 25, "tech_mins": 30, "color": "#A90A30", "sort_order": 10},
    {"name": "Sick Pet Visit", "description": "Business-hours visit for illness, injury concerns, vomiting, diarrhea, limping, skin, ear, eye, or behavior changes.", "duration_mins": 40, "doctor_mins": 35, "tech_mins": 40, "color": "#5E101D", "sort_order": 20},
    {"name": "Dental Consultation", "description": "Dental exam and care planning for oral health concerns or preventive dentistry.", "duration_mins": 30, "doctor_mins": 25, "tech_mins": 30, "color": "#869F12", "sort_order": 30},
    {"name": "Surgery Consultation", "description": "Consultation for surgical care, mass checks, spay/neuter questions, or procedure planning.", "duration_mins": 40, "doctor_mins": 35, "tech_mins": 40, "color": "#B5AC98", "sort_order": 40},
    {"name": "Tech Appointment", "description": "Technician-supported visit such as nail trims, weight checks, or services directed by the medical team.", "duration_mins": 20, "doctor_mins": 0, "tech_mins": 20, "color": "#545454", "sort_order": 50},
]

HOURS = {
    0: (True, 9 * 60, 18 * 60),
    1: (True, 9 * 60, 17 * 60),
    2: (False, 9 * 60, 17 * 60),
    3: (True, 9 * 60, 18 * 60),
    4: (True, 9 * 60, 17 * 60),
    5: (True, 8 * 60, 12 * 60),
    6: (False, 9 * 60, 17 * 60),
}

async def seed_booking() -> None:
    async with AsyncSessionLocal() as db:
        res = await db.execute(select(StaffConfig).limit(1))
        staff = res.scalar_one_or_none()
        if not staff:
            db.add(StaffConfig(num_doctors=1, num_techs=2, slot_granularity_mins=30, booking_window_days=21, min_lead_time_hours=2))
        else:
            staff.num_doctors = staff.num_doctors or 1
            staff.num_techs = max(staff.num_techs or 0, 2)
            staff.slot_granularity_mins = 30
            staff.booking_window_days = max(staff.booking_window_days or 0, 21)
            staff.min_lead_time_hours = 2

        for dow, (is_open, open_mins, close_mins) in HOURS.items():
            res = await db.execute(select(ClinicHours).where(ClinicHours.day_of_week == dow))
            row = res.scalar_one_or_none()
            if row:
                row.is_open = is_open
                row.open_minutes = open_mins
                row.close_minutes = close_mins
            else:
                db.add(ClinicHours(day_of_week=dow, is_open=is_open, open_minutes=open_mins, close_minutes=close_mins))

        for spec in APPOINTMENT_TYPES:
            res = await db.execute(select(AppointmentType).where(AppointmentType.name == spec["name"]))
            row = res.scalar_one_or_none()
            if row:
                for k, v in spec.items():
                    setattr(row, k, v)
                row.active = True
            else:
                db.add(AppointmentType(active=True, **spec))

        await db.commit()
        logger.info("Seeded Cambria booking types and clinic hours")
