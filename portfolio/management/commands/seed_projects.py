from django.core.management.base import BaseCommand
from portfolio.models import Project
PROJECTS=[
 ('SOC — Supervision et détection','Cybersécurité',
  'Mise en place d\'un environnement de supervision centralisé avec Wazuh et ELK pour la détection d\'anomalies.',
  'Wazuh,ELK Stack,Suricata,Linux',
  'Besoin de centraliser les logs et détecter les incidents de sécurité sur l\'infrastructure AMC Assurances pour répondre aux exigences de conformité et améliorer la réactivité face aux attaques.',
  'Architecture SOC : agents Wazuh sur les serveurs, centralisation sur Elasticsearch, visualisation Kibana, règles Suricata pour la détection réseau.',
  'Installation des agents Wazuh sur Windows Server et Linux, configuration des règles de détection, mise en place des alertes et dashboard de monitoring.',
  'Réduction du temps de détection des incidents de 70%, visibilité complète sur l\'infrastructure, alertes automatisées pour les équipes IT.'),
 ('Cloisonnement réseau multisite','Réseaux',
  'Segmentation de trois sites via pare-feu Fortinet et tunnels VPN pour isoler les services critiques.',
  'Fortinet,Cisco,MikroTik,VPN',
  'AMC Assurances avait trois sites interconnectés sans segmentation : un incident sur un site pouvait impacter toute l\'infrastructure. Nécessité d\'isoler les services critiques.',
  'Segmentation en VLANs par service, pare-feu Fortinet en bordure, tunnels VPN IPSec entre sites, règles de filtrage restrictives, DMZ pour les services exposés.',
  'Configuration des policies Fortinet, création des tunnels VPN, tests de connectivité, validation des règles de filtrage, documentation des flux réseau.',
  'Isolation réussie des services, réduction de la surface d\'attaque, résilience améliorée : un incident sur un site n\'impacte plus les autres.'),
 ('Sauvegarde et disponibilité des serveurs','Infrastructure',
  'Déploiement de Veeam pour la sauvegarde et réplication des serveurs critiques.',
  'Windows Server,Veeam,Infrastructure',
  'Absence de solution de sauvegarde centralisée, risque de perte de données en cas de défaillance. Besoin de RPO < 1h et RTO < 4h pour les services critiques.',
  'Serveur Veeam Backup & Replication, réplication vers site secondaire, jobs de sauvegarde incrémentale, stockage sur NAS avec déduplication.',
  'Installation Veeam, configuration des jobs de sauvegarde, tests de restauration, mise en place de la réplication, monitoring des sauvegardes.',
  'RPO de 30 minutes atteint, RTO de 2h validé, suppression du risque de perte de données, conformité PCA/PRA.'),
 ('Active Directory et Microsoft Entra ID','Systèmes',
  'Administration AD avec GPO et synchronisation hybride avec Microsoft Entra ID.',
  'Windows Server,Active Directory,GPO,Entra ID',
  'Travaux pratiques IEF2I pour maîtriser l\'administration d\'un domaine Active Directory et la synchronisation avec le cloud Microsoft.',
  'Contrôleur de domaine Windows Server 2019, OU par service, GPO pour sécurité et configuration, synchronisation Azure AD Connect avec Entra ID.',
  'Création du domaine, configuration des OU, déploiement des GPO (mot de passe, écran de verrouillage, logon scripts), setup Azure AD Connect.',
  'Domaine fonctionnel, stratégies de sécurité appliquées, synchronisation hybride opérationnelle, utilisateurs cloud-on-prem unifiés.'),
 ('Bokoli — Gestion des stagiaires','Développement',
  'Application Django pour la gestion administrative des stagiaires.',
  'Python,Django,PostgreSQL',
  'Projet de développement pour automatiser la gestion des stagiaires : suivi des conventions, évaluations, documents et planning.',
  'Architecture Django MVT, base PostgreSQL, authentification Django, templates Bootstrap, API REST pour intégration future.',
  'CRUD stagiaires, génération PDF conventions, dashboard admin, notifications email, gestion des rôles (admin, tuteur, stagiaire).',
  'Application déployée en production, réduction du temps administratif de 60%, centralisation de toutes les informations stagiaires.'),
 ('Continuité d\'activité ISO 22301','Gouvernance',
  'Pilotage SMCA : analyse d\'impact, définition RTO/RPO et plan de continuité.',
  'ISO 22301,BIA,PCA,PRA',
  'AMC Assurances nécessite une certification ISO 22301 pour garantir la continuité des services métiers critiques en cas d\'incident majeur.',
  'SMCA basé sur ISO 22301, BIA pour identifier les processus critiques, plans PCA/PRA par service, exercices de crise réguliers.',
  'Conduite du BIA avec les métiers, définition des RTO/RPO, rédaction des plans de continuité, organisation des exercices de simulation.',
  'SMCA certifié ISO 22301, 12 processus critiques identifiés, plans de continuité opérationnels, résilience organisationnelle validée.')]
class Command(BaseCommand):
 help='Crée des projets de démonstration modifiables depuis l\'administration'
 def handle(self,*args,**kwargs):
  for i,(title,category,summary,technologies,context,architecture,implementation,results) in enumerate(PROJECTS):
   Project.objects.update_or_create(title=title,defaults={'category':category,'summary':summary,'technologies':technologies,'context':context,'architecture':architecture,'implementation':implementation,'results':results,'order':i})
  self.stdout.write(self.style.SUCCESS('Projets créés ou mis à jour.'))
