from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import tempfile

def export_analytics_pdf(
    mse, r2,
    avg_score, max_score, min_score,
    fig_regression, fig_clusters
):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    c = canvas.Canvas(temp_file.name, pagesize=A4)
    width, height = A4

    # ---------- Title ----------
    c.setFont("Helvetica-Bold", 18)
    c.drawString(1 * inch, height - 1 * inch, "StudyTrack Analytics Report")

    c.setFont("Helvetica", 11)
    c.drawString(1 * inch, height - 1.4 * inch, "AI-based Student Study Habit Analysis")

    # ---------- Metrics ----------
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1 * inch, height - 2.1 * inch, "Key Metrics")

    c.setFont("Helvetica", 11)
    c.drawString(1 * inch, height - 2.5 * inch, f"Average Score: {avg_score}")
    c.drawString(1 * inch, height - 2.9 * inch, f"Highest Score: {max_score}")
    c.drawString(1 * inch, height - 3.3 * inch, f"Lowest Score: {min_score}")
    c.drawString(1 * inch, height - 3.7 * inch, f"MSE: {mse}")
    c.drawString(1 * inch, height - 4.1 * inch, f"R² Score: {r2}")

    # ---------- Charts ----------
    img_y = height - 5.5 * inch

    fig_regression.savefig("regression.png", bbox_inches="tight")
    c.drawImage("regression.png", 1 * inch, img_y, width=5 * inch, height=3 * inch)

    c.showPage()

    fig_clusters.savefig("clusters.png", bbox_inches="tight")
    c.drawImage("clusters.png", 1 * inch, height - 4 * inch, width=5 * inch, height=3 * inch)

    c.save()
    return temp_file.name
