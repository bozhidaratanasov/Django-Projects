from pets.forms.pet_form import PetForm
from django.conf.urls import url
from pets.forms.comment_form import CommentForm
from django.shortcuts import redirect, render
from pets.models import Comment, Pet, Like

def list_pets(request):
    context = {
        'pets' : Pet.objects.all()
    }

    return render(request, 'pet_list.html', context)

def pet_details_or_comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
            'form': CommentForm(),
        }

        return render(request, 'pet_detail.html', context)

    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(comment=form.cleaned_data['text'])
            comment.pet = pet
            comment.save()
            return redirect('pet details or comment', pk)
            
        context = {
            'pet': pet,
            'form': CommentForm(),
        }

        return render(request, 'pet_detail.html', context)

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
            pet = form.save()
            return redirect('list pets')

        context = {
            'form': form,
        }

        return render(request, f'pet_edit.html', context)

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

def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like()
    like.pet = pet
    like.save()
    return redirect('pet details or comment', pk)


def comment_pet(request, pk):
    pass