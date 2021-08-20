from pets.forms.pet_form import PetForm
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from pets.forms.comment_form import CommentForm
from django.shortcuts import redirect, render
from pets.models import Comment, Pet, Like

def list_pets(request):
    context = {
        'pets' : Pet.objects.all()
    }

    return render(request, 'pet_list.html', context)

@login_required
def pet_details_or_comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
            'form': CommentForm(),
            'can_edit_or_delete': request.user == pet.user.user,
            'can_like': request.user != pet.user.user,
            'has_liked': pet.like_set.filter(user_id=request.user.userprofile.id).exists(),
            'can_comment': request.user != pet.user.user,
        }

        return render(request, 'pet_detail.html', context)

    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(comment=form.cleaned_data['text'])
            comment.pet = pet
            comment.user = request.user.userprofile
            comment.save()
            return redirect('pet details or comment', pk)
            
        context = {
            'pet': pet,
            'form': CommentForm(),
        }

        return render(request, 'pet_detail.html', context)

@login_required
def create_pet(request):
    if request.method == 'GET':
        form = PetForm()

        context = {
            'form': form,
        }

        return render(request, 'pet_create.html', context)
    else:
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = Pet(user=request.user.userprofile)
            pet.type = form.cleaned_data['type']
            pet.name = form.cleaned_data['name']
            pet.age = form.cleaned_data['age']
            pet.description = form.cleaned_data['description']
            pet.image = form.cleaned_data['image']
            pet.save()
            return redirect('list pets')

        context = {
            'form': form,
        }

        return render(request, f'pet_edit.html', context)

@login_required
def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        form = PetForm(instance=pet)

        context = {
            'form': form,
            'pet': pet
        }

        return render(request, 'pet_edit.html', context)

    else:
        form = PetForm(
            request.POST,
            request.FILES,
            instance=pet
        )

        if form.is_valid():
            form.save()
            return redirect('pet details or comment', pet.pk)
        
        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, 'pet_edit.html', context)


@login_required
def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet
        }

        return render(request, 'pet_delete.html', context)

    else:
        pet.image.delete()
        pet.delete()
        return redirect('list pets')

@login_required
def like_pet(request, pk):
    like = Like.objects.filter(user_id=request.user.userprofile.id, pet_id=pk).first()
    if like:
        like.delete()
    else:
        pet = Pet.objects.get(pk=pk)
        like = Like(user=request.user.userprofile)
        like.pet = pet
        like.save()
    return redirect('pet details or comment', pk)

