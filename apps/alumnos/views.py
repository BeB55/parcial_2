from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.core.mail import EmailMessage
from reportlab.pdfgen import canvas
from io import BytesIO
from .models import Alumno
import os

@login_required
def enviar_pdf(request, alumno_id):
    alumno = get_object_or_404(Alumno, id=alumno_id, usuario=request.user)

    
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.setFont("Helvetica", 12)
    p.drawString(100, 750, f"Alumno: {alumno.nombre} {alumno.apellido}")
    p.drawString(100, 730, f"Curso: {alumno.curso}")
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    
    email = EmailMessage(
        subject="Datos del alumno",
        body="Adjunto PDF con los datos del alumno.",
        from_email=os.environ.get("DEFAULT_FROM_EMAIL"),
        to=[request.user.email],  # 👈 se lo envía al usuario logueado
    )
    email.attach("alumno.pdf", pdf, "application/pdf")
    email.send()

    return redirect("dashboard")
