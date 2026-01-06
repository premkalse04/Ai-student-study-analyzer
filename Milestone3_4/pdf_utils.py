from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


def export_analytics_pdf(df, mse, r2, cluster_summary_df):
    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    elements = []

    # =========================================================
    # Title
    # =========================================================
    elements.append(Paragraph("<b>StudyTrack – Analytics Report</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    elements.append(
        Paragraph(
            "This report summarizes analytical insights derived from student study habit data, "
            "including performance metrics and habit-based clustering.",
            styles["BodyText"]
        )
    )
    elements.append(Spacer(1, 20))

    # =========================================================
    # Model Metrics
    # =========================================================
    elements.append(Paragraph("<b>Model Performance</b>", styles["Heading2"]))
    elements.append(Spacer(1, 8))

    metrics_table = Table(
        [
            ["Metric", "Value"],
            ["Mean Squared Error (MSE)", f"{mse:.2f}"],
            ["R² Score", f"{r2:.2f}"]
        ],
        colWidths=[200, 200]
    )

    metrics_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"),
    ]))

    elements.append(metrics_table)
    elements.append(Spacer(1, 20))

    # =========================================================
    # Cluster Summary
    # =========================================================
    elements.append(Paragraph("<b>Cluster Summary</b>", styles["Heading2"]))
    elements.append(Spacer(1, 8))

    cluster_data = [cluster_summary_df.columns.tolist()] + cluster_summary_df.reset_index().values.tolist()

    cluster_table = Table(cluster_data)
    cluster_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"),
    ]))

    elements.append(cluster_table)

    # =========================================================
    # Build PDF
    # =========================================================
    doc.build(elements)
    buffer.seek(0)
    return buffer
