from django.contrib.postgres import forms
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import FirewallRuleForm
from django.core.management import call_command
from django.shortcuts import render
from .models import FirewallRule
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
import paramiko
from django.shortcuts import render, redirect
from .models import NatRule


def clear_nat_rules(request):
    NatRule.objects.all().delete()
    return redirect('nat_table')

class NatRuleForm(forms.ModelForm):
    class Meta:
        model = NatRule
        fields = ('src_ip', 'src_port', 'dst_ip', 'dst_port', 'protocol', 'action')


def create_nat_rule(request):
    if request.method == 'POST':
        form = NatRuleForm(request.POST)
        if form.is_valid():
            nat_rule = form.save()
            return redirect('nat_rule_list')
    else:
        form = NatRuleForm()
    return render(request, 'create_nat_rule.html', {'form': form})


def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'Home.html')


def base(request):
    return render(request, 'base.html')


def firewall_rules(request):
    firewall_rules = FirewallRule.objects.all()
    return render(request, 'firewall_rules.html', {'firewall_rules': firewall_rules})


def firewall_rules_form(request):
    return render(request, 'firewall_rules_form.html')


def user_create(request):
    return render(request, 'user_create.html')


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


def delete_rule(rule_id):
    try:
        # Try to get the firewall rule with the given id
        rule = FirewallRule.objects.get(pk=rule_id)
        # Delete the rule
        rule.delete()
        # Return a success response
        return JsonResponse({'status': 'success'})
    except FirewallRule.DoesNotExist:
        # If the rule doesn't exist, return a failure response
        return JsonResponse({'status': 'failure'})


class FirewallRuleCreateView(CreateView):
    form_class = FirewallRuleForm
    template_name = 'add_rules.html'
    success_url = reverse_lazy('about')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Connect to the firewall
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname='firewall_ip', username='firewall_username', password='firewall_password')

        # Execute a command to retrieve the firewall rules
        stdin, stdout, stderr = ssh_client.exec_command('iptables -L')

        # Retrieve the output
        firewall_rules = stdout.read().decode('utf-8')

        # Apply the new firewall rule
        ssh_client.exec_command(form.cleaned_data['rule'])

        # Close the connection
        ssh_client.close()

        return response

    def add_rule(request):
        def add_rule(request):
            rule_name = request.POST.get('rule_name')
            rule_description = request.POST.get('rule_description')
            rule = request.POST.get('rule')

            # Create a new chain
            chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "MY_CHAIN")
            #ipct is iptables just not configured
            # Create a new rule
            new_rule = iptc.Rule()
            new_rule.src = "192.168.1.0/24"
            new_rule.protocol = "tcp"
            new_rule.dst = "192.168.1.5"
            new_rule.target = iptc.Target(new_rule, "ACCEPT")

            # Append the rule to the chain
            chain.insert_rule(new_rule)
        except Exception as e:
            messages.error(request, "An error occurred while adding the rule: {}".format(e))
        return redirect('base')

def delete_rule(request, rule_id):
    try:
        # Try to get the firewall rule with the given id
        rule = FirewallRule.objects.get(pk=rule_id)
        # Delete the rule
        rule.delete()
        # Return a success response
        return JsonResponse({'status': 'success'})
    except FirewallRule.DoesNotExist:
        # If the rule doesn't exist, return a failure response
        return JsonResponse({'status': 'failure'})


def modify_rule(request, rule_id):
    if request.method == 'POST':
        # code to handle the form submission and update the firewall rule
        return redirect('firewall_rules')
    else:
        rule = FirewallRule.objects.get(pk=rule_id)
        form = FirewallRuleForm(instance=rule)
    return render(request, 'modify_rule.html', {'form': form, 'rule': rule})


def get_firewall_rules(request):
    rules = FirewallRule.objects.all()
    rules_data = []
    for rule in rules:
        rules_data.append({'name': rule.name, 'rule': rule.rule})
    return JsonResponse(rules_data, safe=False)


def apply_firewall_rules():
    return None