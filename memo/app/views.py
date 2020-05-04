from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_POST

from .forms import MemoForm
from .models import Memo


def index(req: HttpRequest) -> HttpResponse:
    memos = Memo.objects.all().order_by("-updated_at")
    return render(req, "app/index.html", {"memos": memos})


def detail(req: HttpRequest, memo_id: int) -> HttpResponse:
    memo = get_object_or_404(Memo, id=memo_id)
    return render(req, "app/detail.html", {"memo": memo})


def new_memo(req: HttpRequest) -> HttpResponse:
    if req.method == "POST":
        form = MemoForm(req.POST)
        if form.is_valid:
            form.save()
            return redirect("app:index")

    form = MemoForm
    return render(req, "app/new_memo.html", {"form": form})


@require_POST
def delete_memo(req: HttpRequest, memo_id: int) -> HttpRequest:
    memo = get_object_or_404(Memo, id=memo_id)
    memo.delete()
    return redirect("app:index")


def edit_memo(req: HttpRequest, memo_id: int) -> HttpResponse:
    memo = get_object_or_404(Memo, id=memo_id)
    if req.method == "POST":
        form = MemoForm(req.POST, instance=memo)
        if form.is_valid:
            form.save()
            return redirect("app:index")
    else:
        form = MemoForm(instance=memo)
    return render(req, "app/edit_memo.html", {"form": form, "memo": memo})
