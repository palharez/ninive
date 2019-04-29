from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort
from sgb import db
from sgb.controllers.funcionario import login_required

bp = Blueprint('landing', __name__)


@bp.route('/landing')
@login_required
def index():
    """Exibe a landing page."""
    try:
        return render_template('landing/index.html')
    except:
        return render_template('404.html')
